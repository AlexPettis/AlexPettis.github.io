# Fix up a URL that will fetch the XML document
$url = "https://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?zipCodeList=28607&product=time-series&begin=2023-04-11T00:00:00&end=2023-04-18T00:00:00&maxt=maxt&mint=mint"

# Get the resulting response object from the web service, the
# payload (xml) will be in the .Content property of the object
$response = Invoke-WebRequest -uri $url

# Create a data row that can be passed to the Write-SqlTableData cmdlet,
# which will have a property value for each column in the table.
$row = @([PSCustomObject]@{ Id = 0; EntryDate = [System.DateTime]::Now; Content = $response.Content })

# Import the SqlServer module to get access to the Write-SqlTableData cmdlet
import-module sqlserver

# Call the Write-SqlTableData cmdlet
Write-SqlTableData -serverinstance 'cis-sql.its.appstate.edu' -databasename 'CIS5630' -schemaname dbo -tablename 'DocumentImport' -inputdata $row