function addCrop() {

    if ($('#cropType').val() === 'None') {
        $('#cropType').focus()
        showErrorToast('Please select crop type')
        return false;
    } else if ($('#cropName').val().trim() === '') {
        $('#cropName').focus()
        showErrorToast('Please enter crop name')
        return false;
    } else if ($('#cropDescription').val().trim() === '') {
        $('#cropDescription').focus()
        showErrorToast('Please enter crop description')
        return false;
    } else {
        return true;
    }
}

function addPrice() {

    if ($('#priceChartCropId').val() === 'None') {
        $('#priceChartCropId').focus()
        showErrorToast('Please select crop type')
        return false;
    } else if ($('#cropPrice').val().trim() === '') {
        $('#cropPrice').focus()
        showErrorToast('Please enter crop price')
        return false;
    } else {
        return true;
    }
}


function addVehicle() {

    if ($('#vehicleType').val() === 'None') {
        $('#vehicleType').focus()
        showErrorToast('Please select vehicle type')
        return false;
    } else if ($('#vehicleNumber').val().trim() === '') {
        $('#vehicleNumber').focus()
        showErrorToast('Please enter vehicle number')
        return false;
    } else if ($('#vehicleCharge').val().trim() === '') {
        $('#vehicleCharge').focus()
        showErrorToast('Please enter vehicle charge')
        return false;
    } else {
        return true;
    }
}


function register() {

    if ($('#firstName').val().trim() === '') {
        $('#firstName').focus()
        showErrorToast('Please enter first name')
        return false;
    } else if ($('#lastName').val().trim() === '') {
        $('#lastName').focus()
        showErrorToast('Please enter last name')
        return false;
    } else if ($('#gender').val() === 'None') {
        $('#gender').focus()
        showErrorToast('Please select gender')
        return false;
    } else if ($('#address').val().trim() === '') {
        $('#address').focus()
        showErrorToast('Please enter address')
        return false;
    } else if ($('#contactNumber').val().trim() === '') {
        $('#contactNumber').focus()
        showErrorToast('Please enter contact number')
        return false;
    } else if ($('#userName').val().trim() === '') {
        $('#userName').focus()
        showErrorToast('Please enter user name')
        return false;
    } else {
        return true;
    }
}


function addTimeslot() {

    if ($('#timeslotType').val() === 'None') {
        $('#timeslotType').focus()
        showErrorToast('Please select timeslot type')
        return false;
    } else if ($('#timeslotCapacity').val().trim() === '') {
        $('#timeslotCapacity').focus()
        showErrorToast('Please enter timeslot capacity')
        return false;
    } else {
        return true;
    }
}


function sellRequest() {

    if ($('#cropTypeId').val() === 'None') {
        $('#timeslotType').focus()
        showErrorToast('Please select crop type')
        return false;
    } else if ($('#cropNameId').val() === 'None') {
        $('#cropNameId').focus()
        showErrorToast('Please select crop name')
        return false;
    } else if ($('#cropRequestQuantity').val().trim() === '') {
        $('#cropRequestQuantity').focus()
        showErrorToast('Please enter crop quantity')
        return false;
    } else if ($('#cropRequestDescription').val().trim() === '') {
        $('#croprequestdescription').focus()
        showErrorToast('Please enter crop description')
        return false;
    } else {
        return true;
    }
}


function login() {

    if ($('#loginUsername').val().trim() === '') {
        $('#loginusername').focus()
        showErrorToast('Please enter username')
        return false;
    } else if ($('#loginPassword').val().trim() === '') {
        $('#loginPassword').focus()
        showErrorToast('Please enter password')
        return false;
    } else {
        return true;
    }
}


function bookingSlot() {

    if ($('#bookingNameId').val() === 'None') {
        $('#bookingNameId').focus()
        showErrorToast('Please select crop name')
        return false;
    } else if ($('#bookingDate').val().trim() === '') {
        $('#bookingDate').focus()
        showErrorToast('Please enter booking date')
        return false;
    } else if ($('#bookingSlot').val() === 'None') {
        $('#bookingSlot').focus()
        showErrorToast('Please enter booking slot')
        return false;
    } else {
        return true;
    }
}


function complain() {

    if ($('#complainSubject').val().trim() === '') {
        $('#complainSubject').focus()
        showErrorToast('Please enter complain subject')
        return false;
    } else if ($('#complainDescription').val().trim() === '') {
        $('#complainDescription').focus()
        showErrorToast('Please enter complain description')
        return false;
    } else {
        return true;
    }
}


function feedback() {

    if ($('#feedbackDescription').val().trim() === '') {
        $('#feedbackDescription').focus()
        showErrorToast('Please enter feeback description')
        return false;
    }
    else {
        return true;
    }
}