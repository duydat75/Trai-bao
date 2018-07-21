var BMI_Controller = {

    init: function() {
        BMI_Controller.setForm();
        $("#BMI_Tables_FancyBox").fancybox({
            type: 'inline'
        });
    },

    setForm: function() {
        var bmicalcForm = $('.bmicalc-form');
        bmicalcForm.submit(function(e) {
            e.preventDefault();
            BMI_Controller.calculateBMI(bmicalcForm);
        })
    },

    calculateBMI: function(form) {
        var gender = form.find('#gender input:radio:checked').val();
        var age = form.find('#age').val();
        var weight = parseFloat(form.find('#weight').val());
        var height = parseFloat(form.find('#height').val()) / 100;
        var result = 0;
        var description = "";

        result = BMI_Service.getIndex(weight, height);
        BMI_Controller.showResult(result);

        description = BMI_Service.getDescription(result, gender, age);
        BMI_Controller.showDescription(description);
    },

    showResult: function(result) {
        var bmicalcResult = $('.bmicalc-result');
        bmicalcResult.html(result);
    },

    showDescription: function(description) {
        var bmicalcDescription = $('.bmicalc-description');
        bmicalcDescription.html(description);
    }

};

var BMI_Service = {

    getIndex: function(weight, height) {
        if (isNaN(weight) || isNaN(height)) {
            return '<span class="text-danger">Error</span>';
        } else if (typeof(weight) === 'number' && typeof(height) === 'number') {
            return parseFloat((weight / Math.pow(height, 2)).toFixed(2));
        }
        return null;
    },

    getDescription: function(bmi, gender, age) {
        if (typeof(bmi) === 'number') {
            if (typeof(gender) !== 'undefined' && typeof(age) !== 'undefined') {
                if (gender == 'Male') {
                    switch (age) {
                        case '19 - 24':
                            if (bmi < 20) {
                                return '<div class="p-5   text-warning">Underweight</div>';
                            } else if (bmi > 25) {
                                return '<div class="p-5   text-danger">Over Weight</div>';
                            } else {
                                return '<div class="p-5   text-success">Normal Weight</div>';
                            }
                            break;
                        case '25 - 34':
                            if (bmi < 21) {
                                return '<div class="p-5   text-warning">Underweight</div>';
                            } else if (bmi > 26) {
                                return '<div class="p-5   text-danger">Over Weight</div>';
                            } else {
                                return '<div class="p-5   text-success">Normal Weight</div>';
                            }
                            break;
                        case '35 - 44':
                            if (bmi < 22) {
                                return '<div class="p-5   text-warning">Underweight</div>';
                            } else if (bmi > 27) {
                                return '<div class="p-5   text-danger">Over Weight</div>';
                            } else {
                                return '<div class="p-5   text-success">Normal Weight</div>';
                            }
                            break;
                        case '45 - 54':
                            if (bmi < 23) {
                                return '<div class="p-5   text-warning">Underweight</div>';
                            } else if (bmi > 28) {
                                return '<div class="p-5   text-danger">Over Weight</div>';
                            } else {
                                return '<div class="p-5   text-success">Normal Weight</div>';
                            }
                            break;
                        case '55 - 64':
                            if (bmi < 24) {
                                return '<div class="p-5   text-warning">Underweight</div>';
                            } else if (bmi > 29) {
                                return '<div class="p-5   text-danger">Over Weight</div>';
                            } else {
                                return '<div class="p-5   text-success">Normal Weight</div>';
                            }
                            break;
                        default: // > 64
                            if (bmi < 25) {
                                return '<div class="p-5   text-warning">Underweight</div>';
                            } else if (bmi > 30) {
                                return '<div class="p-5   text-danger">Over Weight</div>';
                            } else {
                                return '<div class="p-5   text-success">Normal Weight</div>';
                            }
                    }
                } else if (gender == 'Female') {
                    switch (age) {
                        case '19 - 24':
                            if (bmi < 19) {
                                return '<div class="p-5   text-warning">Underweight</div>';
                            } else if (bmi > 24) {
                                return '<div class="p-5   text-danger">Over Weight</div>';
                            } else {
                                return '<div class="p-5   text-success">Normal Weight</div>';
                            }
                            break;
                        case '25 - 34':
                            if (bmi < 20) {
                                return '<div class="p-5   text-warning">Underweight</div>';
                            } else if (bmi > 25) {
                                return '<div class="p-5   text-danger">Over Weight</div>';
                            } else {
                                return '<div class="p-5   text-success">Normal Weight</div>';
                            }
                            break;
                        case '35 - 44':
                            if (bmi < 21) {
                                return '<div class="p-5   text-warning">Underweight</div>';
                            } else if (bmi > 26) {
                                return '<div class="p-5   text-danger">Over Weight</div>';
                            } else {
                                return '<div class="p-5   text-success">Normal Weight</div>';
                            }
                            break;
                        case '45 - 54':
                            if (bmi < 22) {
                                return '<div class="p-5   text-warning">Underweight</div>';
                            } else if (bmi > 27) {
                                return '<div class="p-5   text-danger">Over Weight</div>';
                            } else {
                                return '<div class="p-5   text-success">Normal Weight</div>';
                            }
                            break;
                        case '55 - 64':
                            if (bmi < 23) {
                                return '<div class="p-5   text-warning">Underweight</div>';
                            } else if (bmi > 28) {
                                return '<div class="p-5   text-danger">Over Weight</div>';
                            } else {
                                return '<div class="p-5   text-success">Normal Weight</div>';
                            }
                            break;
                        default: // > 64
                            if (bmi < 24) {
                                return '<div class="p-5   text-warning">Underweight</div>';
                            } else if (bmi > 29) {
                                return '<div class="p-5   text-danger">Over Weight</div>';
                            } else {
                                return '<div class="p-5   text-success">Normal Weight</div>';
                            }
                    }
                }
            }
            return '<span class="text-danger">Missing Entries</span>';
        }

        return '<span class="text-danger">Invalid Entries</span>';
    }

};

// initialization
BMI_Controller.init();