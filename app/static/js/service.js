/**
 * Created by ayach on 11/05/17.
 */
angular.module('myApp', [])
            .controller('DashCtrl', function($scope, $http) {

                $scope.info = {};
                var programme = [];

                $scope.showConnect = true;

                $scope.executesh = function () {
                     $("#cont").css("display","none");
                   $("#loading").css("display","block");
                     $('#check :checked').each(function() {
                         var p = {id:'',name:''}
                         p.id=$(this).attr('alt');
                         p.name=$(this).attr('name');
                         programme.push(p);
                                                });
                   var id = $('#btn_install').attr('name');
                   var oracle  = {user:'',sid:''};
                   oracle.sid= $("#oracle-sid").val();
                   oracle.user =$("#oracle-user").val();
                   var folderinstaller = $("#installer-user").val();
					$scope.con = {};
					$http({
						method: 'POST',
						url: '/ssh/execute',
						data: {id:id,program:programme,folder:folderinstaller,oracle:oracle}
					}).then(function(response) {
						console.log(response);
						$scope.con = response.data;
						 $("#cont").css("display","block");
                         $("#loading").css("display","none");
					}, function(error) {
					     $("#cont").css("display","block");
                         $("#loading").css("display","none");
						console.log(error);
					});
                }

                $scope.database = function () {
                    var db = {username:'',pass:'',sid:'',schema:'',dumpfile:'',remptarget:'',rempsource:'',logfile:'',type:''}
                    db.type = $('#tel :checked').val();
                    db.username =$('#username_db').val();
                    db.pass =$('#password_db').val();
                    db.sid=$('#data_base_db').val();
                    db.schema=$('#schema_db').val();
                    db.dumpfile=$('#dumpfile_db').val();
                    db.remptarget=$('#remap_target_name').val();
                    db.rempsource=$('#remap-src_name').val();
                    db.logfile=$('#logfile_name').val();
                    var id =$('#btn_sub_db').attr('name');
                    $http({
						method: 'POST',
						url: '/ssh/dbase',
						data: {id:id,db:db}
					}).then(function(response) {
						console.log(response);
						$scope.con = response.data;
						 $("#cont").css("display","block");
                         $("#loading").css("display","none");
					}, function(error) {
					     $("#cont").css("display","block");
                         $("#loading").css("display","none");
						console.log(error);

					});

                }
                $scope.solifeinst = function () {
                    var solife = {path:'',jbhost:'',host:'',sid:'',dbuser:'',jbhome:'',jvhome:'',port:'',action:''}
                    solife.path=$('#path_solife').val();
                    solife.jbhost=$('#jb_host_solife').val();
                    solife.host=$('#host_solifedb').val();
                    solife.sid=$('#sid_solife').val();
                    solife.dbuser=$('#db_user_solife').val();
                    solife.jbhome=$('#jb_home').val();
                    solife.jvhome=$('#java_home').val();
                    solife.port=$('#port_solife').val();
                    solife.action=$('#action :checked').val();
                    $http({
						method: 'POST',
						url: '/ssh/solife',
						data: {id:id,solife:solife}
					}).then(function(response) {
						console.log(response);
						$scope.con = response.data;
						 $("#cont").css("display","block");
                         $("#loading").css("display","none");
					}, function(error) {
					     $("#cont").css("display","block");
                         $("#loading").css("display","none");
						console.log(error);
					});
                }
            });