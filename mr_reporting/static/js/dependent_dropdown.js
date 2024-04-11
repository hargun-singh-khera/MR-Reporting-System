function getCurrentUrl() {
    return window.location.origin + window.location.pathname;
}

function countryfield() {
    var countryDropdown = document.getElementById('id_country');
    if (countryDropdown) {
        var countryId = countryDropdown.value;
        window.location = getCurrentUrl() + "?country=" + countryId;
    }
}

function statefield() {
    var stateDropdown = document.getElementById('id_state');
    if (stateDropdown) {
        var countryId = document.getElementById('id_country').value;
        var stateId = stateDropdown.value;
        window.location = getCurrentUrl() + "?country=" + countryId + "&state=" + stateId;
    }
}

function employeefield() {
    var employeeDropdown = document.getElementById('id_employee');
    if (employeeDropdown) {
        var employeeId = employeeDropdown.value;
        window.location = getCurrentUrl() + "?employee=" + employeeId;
    }
}

function areafield() {
    var areaDropdown = document.getElementById('id_area_from');
    if (areaDropdown) {
        var employee = document.getElementById('id_employee').value;
        var areaId = areaDropdown.value;
        window.location = getCurrentUrl() + "?country=" + countryId + "&area=" + areaId;
    }
}

document.addEventListener('DOMContentLoaded', function() {
    console.log("Javascript loaded");

    var countryDropdown = document.getElementById('id_country');
    var stateDropdown = document.getElementById('id_state');
    var employeeDropdown = document.getElementById('id_employee');
    var areaDropdown = document.getElementById('id_area');

    if (countryDropdown) {
        countryDropdown.addEventListener('change', countryfield);
    }

    if (stateDropdown) {
        stateDropdown.addEventListener('change', statefield);
    }

    if(employeeDropdown) {
        employeeDropdown.addEventListener('change', employeefield);
    }
    
    if(areaDropdown) {
        areaDropdown.addEventListener('change', areafield);
    }
});
