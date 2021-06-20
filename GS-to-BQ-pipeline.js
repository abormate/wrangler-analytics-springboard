function loadToBQ() {

  var projectId = 'lowercase project name within quotes';
  var datasetId = 'dataset name within quotes';
  var yestDate = new Date();
  yestDate.setDate(yestDate.getDate()-2);
  var formattedDate = Utilities.formatDate(yestDate, "GMT", "yyyyMMdd");
  var tableId = 'name of new table within quotes, no spaces';
  var fileId = 'the alphanumeric number in Google Sheets URL between d/ and /edit (within quotes)';

  // Define our load job.
  var jobSpec = {
    configuration: {
      load: {
        destinationTable: {
          projectId: projectId,
          datasetId: datasetId,
          tableId: tableId
        },
        allowJaggedRows: true,
        writeDisposition: 'WRITE_APPEND',
        schema: {
          fields: [
            {name:'date', type: 'STRING'},
            {name:'source', type: 'STRING'},
            {name:'medium', type: 'STRING'},
            {name:'campaign', type: 'STRING'},
            {name:'adContent', type: 'STRING'},
            {name:'sessions', type: 'STRING'},
            {name:'pageviews', type: 'STRING'}
          ]
        }
      }
    }
  };

  var spreadsheet = SpreadsheetApp.openById(fileId);
  var filename = spreadsheet.getName();
  
  var MAX_ROWS = 5000;
  var sheet = spreadsheet.getSheets()[0]; 
  var data = sheet.getDataRange().getValues();
  var csvdata = "";
  for (var row = 1; row < data.length && row < MAX_ROWS + 1; row++) {
    for (var col = 0; col < data[row].length; col++) {
      var cell = data[row][col].toString();
      if (cell.indexOf(",") != -1) {
        csvdata += "\"" + cell + "\"";
      } else {
        csvdata += cell;
      }

      if (col < data[row].length - 1) {
        csvdata += ",";
      }
    }
    csvdata += "\r\n";
  }
  var data = Utilities.newBlob(csvdata, "application/octet-stream");

  // Execute the job.
  BigQuery.Jobs.insert(jobSpec, projectId, data);
}
