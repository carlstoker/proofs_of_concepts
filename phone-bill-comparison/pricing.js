var plans = {
    "AT&T Mobile Share Plus 3GB": {
        base: 50,
        dataLimit: 3,
        overageFeePerGB: 0,
        overageFeeCap: 0,
        overageRounding: 0,
        id: 'att3GB'
    },
    "AT&T Mobile Share Plus 9GB": {
        base: 60,
        dataLimit: 9,
        overageFeePerGB: 0,
        overageFeeCap: 0,
        overageRounding: 0,
        id: 'att9GB'
    },
    "AT&T Unlimited": {
        base: 70,
        dataLimit: 0,
        overageFeePerGB: 0,
        overageFeeCap: 0,
        overageRounding: 0,
        id: 'attUnlimited'
    },
   "Google Fi": {
        base: 20,
        dataLimit: 0,
        overageFeePerGB: 10,
        overageFeeCap: 60,
        overageRounding: 2,
        id: 'fi'
    },
    "Sprint Unlimited": {
        base: 60,
        dataLimit: 0,
        overageFeePerGB: 0,
        overageFeeCap: 0,
        overageRounding: 0,
        id: 'sprintUnlimited'
    },
   "T-Mobile Unlimited": {
        base: 70,
        dataLimit: 0,
        overageFeePerGB: 0,
        overageFeeCap: 0,
        overageRounding: 0,
        id: 'tmobileUnlimited'
    },
   "Verizon S (2GB)": {
        base: 55,
        dataLimit: 2,
        overageFeePerGB: 15,
        overageFeeCap: "uncapped",
        overageRounding: 0,
        id: 'verizon2GB'
    },
   "Verizon M (4GB)": {
        base: 70,
        dataLimit: 4,
        overageFeePerGB: 15,
        overageFeeCap: "uncapped",
        overageRounding: 0,
        id: 'verizon4GB'
    },
   "Verizon 5 (5GB)": {
        base: 75,
        dataLimit: 5,
        overageFeePerGB: 15,
        overageFeeCap: "uncapped",
        overageRounding: 0,
        id: 'verizon5GB'
    },
   "Verizon L (8GB)": {
        base: 90,
        dataLimit: 8,
        overageFeePerGB: 15,
        overageFeeCap: "uncapped",
        overageRounding: 0,
        id: 'verizon8GB'
    },
   "Verizon Unlimited": {
        base: 75,
        dataLimit: 0,
        overageFeePerGB: 0,
        overageFeeCap: 0,
        overageRounding: 0,
        id: 'verizonUnlimited'
    }
};

function calculateMonthlyCharge(plan, data) {
    data = data.toFixed(plans[plan]['overageRounding']);
    if (data > plans[plan]['dataLimit']) {
        dataChargedFor = data - plans[plan]['dataLimit'];
        
        dataCharge = dataChargedFor * plans[plan]['overageFeePerGB'];
        if (plans[plan]['overageFeeCap'] != "uncapped") {
            dataCharge = Math.min(dataCharge, plans[plan]['overageFeeCap']);
        }
    }
    else { dataCharge = 0; }
    total = (plans[plan]['base'] + dataCharge).toFixed(2);
    return total;
}

function generateEmptyTable() {
    var arrayLength = Object.keys(plans).length;
    for (var i = 0; i < arrayLength; i++) {
        plan = Object.keys(plans)[i]
        
        let row = document.createElement('div');
        row.className = 'divTableRow';
        row.id = plans[Object.keys(plans)[i]]['id'];
        
        let cell = document.createElement('div');
        cell.className = 'divTableCell';
        row.appendChild(cell);
        
        cell = document.createElement('div');
        cell.className = 'divTableCell';
        row.appendChild(cell);

        document.getElementById('plans').appendChild(row);
    }
}

function dataUpdate(data) {
    var arrayLength = Object.keys(plans).length;
    for (var i = 0; i < arrayLength; i++) {
        plan = Object.keys(plans)[i]
        let monthly = calculateMonthlyCharge(plan, data);
        
        let row = document.getElementById(plans[Object.keys(plans)[i]]['id']);
        row.getElementsByTagName('div')[0].innerText = plan;
        row.getElementsByTagName('div')[1].innerText = '$' + monthly;
    }
}
generateEmptyTable();
dataUpdate(2);