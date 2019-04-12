var localityApi='/get_locality_data/';
var localityData='';
$(document).ready(function () {

    var chartsContext = {
        currentOrgLevel: "national"
    };

    $( ".dropdown-menu li" ).click(function(event) {
        if( $(this).attr("id") == 'national' && chartsContext.currentOrgLevel !='national'){
            fetchHivStatsFromServer('national');
            chartsContext.currentOrgLevel ='national'
        }else if( $(this).attr("id") == 'county' && chartsContext.currentOrgLevel !='county'){
            fetchHivStatsFromServer('county');
            chartsContext.currentOrgLevel ='county';
        }else if( $(this).attr("id") == 'constituency' && chartsContext.currentOrgLevel !='constituency'){
            fetchHivStatsFromServer('constituency');
            chartsContext.currentOrgLevel ='constituency';
        }else if( $(this).attr("id") == 'ward' && chartsContext.currentOrgLevel !='ward'){
            fetchHivStatsFromServer('ward');
            chartsContext.currentOrgLevel ='ward';
        }else {
        }

    });
});


function destroyChosenDropDownList(elementId) {
    try {
        $(elementId).chosen("destroy");
    } catch (err) {
        console.log(err);
    }
}


function populateOrgunitList(data,elementId) {
    $(elementId).empty();
    $(elementId).append("<option></option>");
    $.each(data, function (index, objValue) {
        var elementToAppend = '<option data-id="' + objValue.id + '" data-name="' + objValue.name + '">' + objValue.name + '</option>';
        $(elementId).append(elementToAppend);
    });
}


var initOrganisationUnitChosenDropDown = function initOrganisationUnitChosenDropDown(orgType,id) {
    $(id).chosen({
        placeholder_text_single: "Select " + orgType + ": ",
        no_results_text: "No results found!",
        width: "284px"
    });
};



function cloneObject(obj) {
    var clone = {};
    for (var i in obj) {
        if (obj[i] != null && typeof (obj[i]) == "object")
            clone[i] = cloneObject(obj[i]);
        else
            clone[i] = obj[i];
    }
    return clone;
}

//county event handler
$('#county-organisation-unit').on('change', function (event) {
    var localityDataToDisplay= cloneObject(localityData);
    var selectedCountyId = $("#county-organisation-unit option:selected").attr('data-id');
    var selectedCountyName=$("#county-organisation-unit option:selected").attr('data-name');
    $('.org-unit-label').html(selectedCountyName);
    destroyChosenDropDownList('#countituency-organisation-unit');

    $.each(localityData, function (key, objValue) {  // filter out countituency int that county

        if(key!=selectedCountyId){
            delete localityDataToDisplay[key];
        }
    });
    //enable sub county list element;
    $('#countituency-organisation-unit').prop("disabled", false); // Element(s) are now enabled.
    $.each(localityDataToDisplay, function( key, value ) {
        populateOrgunitList(value.siblings,'#countituency-organisation-unit');
    });

    initOrganisationUnitChosenDropDown("sub county","#countituency-organisation-unit");

});

//sub county event handler
$('#countituency-organisation-unit').on('change', function (event) {
    var selectedCountyId = $("#countituency-organisation-unit option:selected").attr('data-id');
    var selectedSubCountyName=$("#countituency-organisation-unit option:selected").attr('data-name');
    $('.org-unit-label').html(selectedSubCountyName);

});

function fetchOrganisationUnitData(){
    $.ajax({
        type: 'GET', // define the type of HTTP verb we want to use
        url: localityApi, // the url from server we that we want to use
        contentType: 'application/json; charset=utf-8',
        dataType: 'json', // what type of data do we expect back from the server
        encode: true,
        success: function (data, textStatus, jqXHR) {
            localityData=data;
            $.each(data, function( key, value ) {

                var elementToAppend = '<option data-id="' + key + '" data-name="' + value.name + '">' + value.name + '</option>';
                $("#county-organisation-unit").append(elementToAppend);

            });
            initOrganisationUnitChosenDropDown("County:","#county-organisation-unit");
            initOrganisationUnitChosenDropDown("County:","#countituency-organisation-unit");
            console.log("localityData");
            console.log(localityData);
        },
        error: function (response, request) {
            //    console.log("got an error fetching wards");
            var parsed_data = response.responseText;
        }

    });

}
fetchOrganisationUnitData();