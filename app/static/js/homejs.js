/**
 * Created by ayach on 11/05/17.
 */

 var a = parseInt("10");
    console.log('test');
     console.log(a);
$('#Oracle-check').click(function() {
    $("#prop-oracle").toggle(this.checked);
});

$('input[type="radio"]').click(function() {
       if($(this).attr('id') == 'impo')
       {$('#export').css('display','block');}
       else if($(this).attr('id') == 'ex')
       {$('#export').css('display','none');}
       else if($(this).attr('id') == 'inst')
       {$('#sc_update').css('display','none');}
       else if($(this).attr('id') == 'upda')
       {$('#sc_update').css('display','block');}
});

$('#fileuploadoracle').on('change',function() {
      var reader = new FileReader();
      reader.readAsText(event.target.files[0]);
      reader.onloadend = function(event) {
      var xmlDoc = $.parseXML( reader.result );
      var $xml = $( xmlDoc );
      var m = $xml.find("title");
      $('#oracle-sid').val($($xml).find( 'title' ).text());
  }
});
$('#fileuploaddb').on('change',function() {
      var reader = new FileReader();
      reader.readAsText(event.target.files[0]);
      reader.onloadend = function(event) {
      var xmlDoc = $.parseXML( reader.result );
      var $xml = $( xmlDoc );
      $('#username_db').val($($xml).find( 'username' ).text());
      $('#password_db').val($($xml).find( 'password' ).text());
      $('#data_base_db').val($($xml).find( 'database' ).text());
      $('#schema_db').val($($xml).find( 'schema' ).text());
      $('#logfile_name').val($($xml).find( 'logfile' ).text());
      $('#remap-src_name').val($($xml).find( 'remapsource' ).text());
      $('#remap_target_name').val($($xml).find( 'remaptarget' ).text());
      $('#dumpfile_db').val($($xml).find( 'dumpfile' ).text());

  }
});
$('#fileuploadsolife').on('change',function() {
      var reader = new FileReader();
      reader.readAsText(event.target.files[0]);
      reader.onloadend = function(event) {
      var xmlDoc = $.parseXML( reader.result );
      var $xml = $( xmlDoc );
      $('#path_solife').val($($xml).find( 'path' ).text());
      $('#jb_host_solife').val($($xml).find( 'jbosshost' ).text());
      $('#host_solifedb').val($($xml).find( 'hostname' ).text());
      $('#sid_solife').val($($xml).find( 'sid' ).text());
      $('#db_user_solife').val($($xml).find( 'dbuser' ).text());
      $('#Jb_home').val($($xml).find( 'jbosshome' ).text());
      $('#java_home').val($($xml).find( 'javahome' ).text());
      $('#port_solife').val($($xml).find( 'port' ).text());
      $('#folder_solife').val($($xml).find('foldersolife').text());
    }
  });

$( document ).ready(function() {
    console.log('ok');
          var dataPie = [
                    { label: "CPU", color:'#8C54CA', data: 100},
                    { label: "FREE", color:'#58B2F4', data: 70},
                ];

                $.plot('#doughnut-chart', dataPie, {
                    series: {
                        pie: {
                            show: true,
                            innerRadius: 0.4,
                        }
                    },
                    legend: {
                        show: false
                    }
                });
                var dataPie = [
                    { label: "CPU", color:'#8C54CA', data: 100},
                    { label: "FREE", color:'#58B2F4', data: 70},
                ];

                $.plot('#doughnut-chartr', dataPie, {
                    series: {
                        pie: {
                            show: true,
                            innerRadius: 0.4,
                        }
                    },
                    legend: {
                        show: false
                    }
                });
                var dataPie = [
                    { label: "CPU", color:'#8C54CA', data: 100},
                    { label: "FREE", color:'#58B2F4', data: 70},
                ];

                $.plot('#doughnut-chartra', dataPie, {
                    series: {
                        pie: {
                            show: true,
                            innerRadius: 0.4,
                        }
                    },
                    legend: {
                        show: false
                    }
                });

});