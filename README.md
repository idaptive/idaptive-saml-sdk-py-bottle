# IdaptiveSAMLSDK_PyBottle

This is an example on adding SAML to your Python web application (This example uses Bottle but the code will work with any framework). 

This example was created using Python 3.4.3.
This code uses lxml to parse the SAML XML. lxml can be installed via pip (python pip lxml) on Linux and Mac, or by compiling on PC. There are also unoffical binaries compiled with a windows installer that could be used.
This code uses SignXML to validate the SAML Assertions. This can be installed via pip (Windows: python -m pip signxml, Other: python pip signxml) from a console.

You will need a Signing Certificate from an Idaptive SAML Application, and the endpoint URL's from the SAML Application.


If you navigate to http://localhost:6321/, you will start SP Initiated SAML SSO. If you go the User Portal and click the Generic SAML Application you will start IDP Initiated SAML SSO.
