console.log("Dropdown JavaScript loaded")
document.addEventListener('DOMContentLoaded', function() {
    // Get the dropdown elements
    var employeeDropdown = document.getElementById('id_employee');
    var fromAreaDropdown = document.getElementById('id_from_area');
    var toAreaDropdown = document.getElementById('id_from_area');
    

    // Add event listeners to each dropdown
    employeeDropdown.addEventListener('change', function() {
        var selectedEmployeeId = this.value;
        console.log('Selected Employee ID:', selectedEmployeeId);
    });

    // fromAreaDropdown.addEventListener('change', function() {
    //     var selectedFromAreaId = this.value;
    //     console.log('Selected From Area ID:', selectedFromAreaId);
    // });

    // toAreaDropdown.addEventListener('change', function() {
    //     var selectedToAreaId = this.value;
    //     console.log('Selected To Area ID:', selectedToAreaId);
    // });
});