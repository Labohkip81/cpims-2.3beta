    $(document).ready(function () {
        var org_level='national';
        fetchTotalOVCsEver('national',"");
        fetchNewOVCRegs('national',"");
        fetchActiveOVCs('national',"");
    });
    
    function fetchTotalOVCsEver(org_level,area_id){
         $.ajax({
            type: 'GET',
            url: '/get_total_ovc_ever/'+org_level+'/'+area_id+'/',
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            encode: true,
            success: function (data, textStatus, jqXHR) {
                displayTotalOVCsEver(data);
            },
            error: function (response, request) {
                console.log(response.responseText);
            }
        });
    }
    function fetchNewOVCRegs(org_level,area_id){
         $.ajax({
            type: 'GET',
            url: '/hiv_stats_pub_data/'+org_level+'/'+area_id+'/',
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            encode: true,
            success: function (data, textStatus, jqXHR) {
                displayNewOVCRegs(data);
            },
            error: function (response, request) {
                console.log(response.responseText);
            }
        });
    }
    function fetchActiveOVCs(org_level,area_id){
         $.ajax({
            type: 'GET',
            url: '/hiv_stats_pub_data/'+org_level+'/'+area_id+'/',
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            encode: true,
            success: function (data, textStatus, jqXHR) {
                
                displayActiveOVCs(data);
            },
            error: function (response, request) {
                console.log(response.responseText);
            }
    
        });
    }
    



    
    function displayTotalOVCsEver(data){
        var val = data;        
        var elementId="all_ovc_reg";
        // $.each(data, function (index, objValue) {
        //    val += objValue;
        // });
        $('#'+elementId).html(val);
    }
    function displayNewOVCRegs(data){
        // $.each(data, function (index, objValue) {
           var elementId="new_ovc_registrations";
           var the_x_axis= ['Jan 2018', 'Feb 2018', 'Mar 2018', 'Apr 2018', 'May 2018']
           var the_title = 'New OVCs within period';
           var the_series = [
                                { name: 'Female', data: [3896, 3979, 1798, 7687, 4565] },
                                { name: 'Male', data: [1396, 1979, 7908, 4767, 5365] }
                            ];
    
            barChart(elementId,the_title,the_x_axis,the_series)
        // });
    }
    function displayActiveOVCs(data){
        // $.each(data, function (index, objValue) {
           var elementId="active_ovc";
           var the_x_axis= ['Jan 2018', 'Feb 2018', 'Mar 2018', 'Apr 2018', 'May 2018']
           var the_title = 'Active OVCs within period';
           var the_series = [
                                { name: 'Female', data: [3896, 3979, 9798, 1687, 565] },
                                { name: 'Male', data: [396, 979, 798, 767, 565] }
                            ];
    
            barChart(elementId,the_title,the_x_axis,the_series)
        // });
    }
    
    
    
    