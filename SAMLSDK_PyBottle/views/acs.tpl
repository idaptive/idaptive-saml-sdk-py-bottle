% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<h3>{{ message }}</h3>
<hr/>
	% if (success):
<style>
	table {
		width: "60%";
		border: 0;
	}
	td {
		padding: 9px;
		font-size:15px;
	}
</style>
<h3>ACS listed contents:</h3>
<table>
<tr>
	<td>User</td>
	<td>{{userId}}</td>
</tr>
</table>
<hr/>
<h4><a href="/logout">Click here to Logout</a></h4>
	% end