#Main Application

import bottle
import os
import sys
import SAML_Interface
import uuid

from bottle import Bottle, route, view, run, redirect, request, response, ServerAdapter, jinja2_view
from datetime import datetime

if '--debug' in sys.argv[1:] or 'SERVER_DEBUG' in os.environ:
    # Debug mode will enable more verbose output in the console window.
    # It must be set at the beginning of the script.
    bottle.debug(True)

def wsgi_app():
    #Returns the application to make available through wfastcgi. This is used when the site is published to Microsoft Azure.
    return bottle.default_app()

if __name__ == '__main__':
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    PORT = 6321

    @bottle.route('/static/<filepath:path>')
    def server_static(filepath):
        #Handler for static files, used with the development server. When running under a production server such as IIS or Apache, the server should be configured to serve the static files.
        return bottle.static_file(filepath, root=STATIC_ROOT)

#Http Routing

    #Default
    @route('/')
    @route('/default')
    @view('default')
    def default():        
        return dict(
        title='SAML Homepage',
        message='Welcome to the sample SAML web application!',
        year=datetime.now().year
        )
    #ACS
    @route('/acs', method=['GET','POST'])
    @view('acs')
    def acs():
        samlResponse = request.forms['SAMLResponse']
        #ACS URL listed here:
        strAcsUrl = 'http://localhost:6321/acs'
        if SAML_Interface.SAML_Response.ParseSAMLResponse(strAcsUrl,samlResponse)[0]:
            return dict(
                success = True,
                title = 'ACS Successful',
                message = 'SAML Response Was Accepted',
                userId = SAML_Interface.SAML_Response.ParseSAMLResponse(strAcsUrl,samlResponse)[1][1:-1],
                year = datetime.now().year
        )
        else:
            return dict(
                success = False,
                title = 'ACS Unsuccessful',
                message = 'SAML Response Was Not Accepted',
                year = datetime.now().year,
        )
    #Logout
    @route('/logout', method=['GET','POST'])
    @view('logout')
    def logout():
        #Sign Out URL listed here:
        strIdentityProviderSignOutURL = '<SIGN OUT URL HERE>'          
        bottle.redirect('{uIDPUrl}?{bParams}'.format(uIDPUrl = strIdentityProviderSignOutURL, bParams = ''))
    #Login
    @route('/login', method=['GET','POST'])
    @view('login')
    def login():
        strAcsUrl = 'http://localhost:6321/acs'
        #Issuer URL listed here:
        strIssuer = '<ISSUER URL HERE>'
        #Sign In URL listed here:
        strSingleSignOnURL = '<SIGN IN URL HERE>'  
        bottle.redirect('{uIDPUrl}?{bParams}'.format(uIDPUrl = strSingleSignOnURL, bParams = SAML_Interface.SAML_Request.GetSAMLRequest(strAcsUrl, strIssuer)))
   
   # Starts a local test server.
    bottle.run(server='wsgiref', host=HOST, port=PORT)
