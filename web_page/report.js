// var doctor = document.getElementById('doctor');

// function addRow() {
//     var newRow = document.createElement('tr');

//     // Create cells for the new row
//     var selectCell = document.createElement('td');
//     var select = document.createElement('select');
//     select.className = 'form-select';
//     select.setAttribute('aria-label', 'Default select example');
//     select.setAttribute('name', 'doctor');
//     select.setAttribute('required', 'true');
//     var defaultOption = document.createElement('option');
//     defaultOption.setAttribute('selected', 'true');
//     defaultOption.textContent = 'Open this select menu';
//     select.appendChild(defaultOption);
//     var option1 = document.createElement('option');
//     option1.setAttribute('value', '1');
//     option1.textContent = 'One';
//     var option2 = document.createElement('option');
//     option2.setAttribute('value', '2');
//     option2.textContent = 'Two';
//     var option3 = document.createElement('option');
//     option3.setAttribute('value', '3');
//     option3.textContent = 'Three';
//     select.appendChild(option1);
//     select.appendChild(option2);
//     select.appendChild(option3);
//     selectCell.appendChild(select);

//     var departureCell = document.createElement('td');
//     var departureInput = document.createElement('input');
//     departureInput.setAttribute('type', 'time');
//     departureInput.className = 'form-control';
//     departureInput.setAttribute('name', 'departure-time');
//     departureCell.appendChild(departureInput);

//     var arrivalCell = document.createElement('td');
//     var arrivalInput = document.createElement('input');
//     arrivalInput.setAttribute('type', 'time');
//     arrivalInput.className = 'form-control';
//     arrivalInput.setAttribute('name', 'arrival-time');
//     arrivalCell.appendChild(arrivalInput);

//     var buttonCell = document.createElement('td');
//     var button = document.createElement('button');
//     button.className = 'btn btn-danger w-100 remove-row';
//     button.textContent = 'Remove';
//     buttonCell.appendChild(button);

//     // Append cells to the new row
//     newRow.appendChild(selectCell);
//     newRow.appendChild(departureCell);
//     newRow.appendChild(arrivalCell);
//     newRow.appendChild(buttonCell);

//     // Show "Add" button only for the latest row
//     var addButtons = document.getElementsByClassName('add-row');
//     for (var i = 0; i < addButtons.length; i++) {
//         addButtons[i].style.display = 'none';
//     }
//     // Hide "Remove" button for all rows except the last one
//     var removeButtons = document.getElementsByClassName('remove-row');
//     for (var j = 0; j < removeButtons.length; j++) {
//         removeButtons[j].style.display = 'block';
//     }

//     // Append the new row to the table
//     doctor.appendChild(newRow);
// }

// // Attach event listener to the initial "Add" button
// var initialAddButton = document.getElementById('btn-doctor-add');
// initialAddButton.addEventListener('click', addRow);

// // Attach event listener for the "Remove" buttons
// doctor.addEventListener('click', function(event) {
//     if (event.target.classList.contains('remove-row')) {
//         var row = event.target.parentNode.parentNode;
//         row.parentNode.removeChild(row);
//     }
//     // Show "Add" button for the last row after removing any previous "Add" buttons
//     var addButtons = document.getElementsByClassName('add-row');
//     for (var i = 0; i < addButtons.length; i++) {
//         addButtons[i].style.display = 'none';
//     }
//     addButtons[addButtons.length - 1].style.display = 'block';
// });

// // Event listener for the delete button
// var deleteButton = document.getElementById('delete-table');
// deleteButton.addEventListener('click', function() {
//     doctor.innerHTML = ''; // Remove all rows from the table
// });

$(document).ready(function() {
    console.log("Loaded");
    // Add button click event
    $("#btn-doctor-add").click(function() {
        console.log("Add clicked");
        var $clone = $(".doctor-row").first().clone(); // Clone the entire row
        $clone.find("select, input").val(""); // Clear the values of cloned row
        $("#form-fields").append($clone); // Append the cloned row to the table
    });
});

