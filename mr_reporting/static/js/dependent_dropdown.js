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
    console.log("State changed")
    var stateDropdown = document.getElementById('id_state');
    if (stateDropdown) {
        var countryId = document.getElementById('id_country').value;
        var stateId = stateDropdown.value;
        window.location = getCurrentUrl() + "?country=" + countryId + "&state=" + stateId;
    }
} 

function cityfield() {
    console.log("City changed")
    var cityDropdown = document.getElementById('id_city');
    if (cityDropdown) {
        var countryId = document.getElementById('id_country').value;
        var stateId = document.getElementById('id_state').value;
        var cityId = cityDropdown.value;
        window.location = getCurrentUrl() + "?country=" + countryId + "&state=" + stateId + "&city=" + cityId;
    }
} 

function employeefield() {
    var employeeDropdown = document.getElementById('id_employee');
    if (employeeDropdown) {
        var employeeId = employeeDropdown.value;
        window.location = getCurrentUrl() + "?employee=" + employeeId;
    }
}


document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM Loaded");
    var countryDropdown = document.getElementById('id_country');
    var stateDropdown = document.getElementById('id_state');
    var cityDropdown = document.getElementById('id_city');
    var employeeDropdown = document.getElementById('id_employee');

    if (countryDropdown) {
        countryDropdown.addEventListener('change', countryfield);
    }

    if (stateDropdown) {
        stateDropdown.addEventListener('change', statefield);
    }

    if (cityDropdown) {
        cityDropdown.addEventListener('change', cityfield);
    }

    if (employeeDropdown) {
        employeeDropdown.addEventListener('change', employeefield);
    }
    
});
