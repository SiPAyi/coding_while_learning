var boxes = [];
var boxNames = ['box1','box2','box3','box4','box5','box6','box7','box8','box9']

for(let i = 0 ; i<=9 ; i++){
    boxes[i] = document.getElementById(boxNames[i])
}

var cellReference = [['a11','a12','a13','a14','a15','a16','a17','a18','a19'],
['a21','a22','a23','a24','a25','a26','a27','a28','a29'],
['a31','a32','a33','a34','a35','a36','a37','a38','a39'],
['a41','a42','a43','a44','a45','a46','a47','a48','a49'],
['a51','a52','a53','a54','a55','a56','a57','a58','a59'],
['a61','a62','a63','a64','a65','a66','a67','a68','a69'],
['a71','a72','a73','a74','a75','a76','a77','a78','a79'],
['a81','a82','a83','a84','a85','a86','a87','a88','a89'],
['a91','a92','a93','a94','a95','a96','a97','a98','a99']]

var allCells = cellReference;

for(j = 0 ; j <= 8 ; j++){
    for(i = 0 ; i <= 8 ; i++){
        allCells[j][i] = document.getElementById(cellReference[j][i]);
    }
}

function randomValue(){
    randValue = Math.floor(Math.random()*9)
    return randomValue
}

alert(randomValue())

// allCells[randomValue()][randomValue()].innerHTML = randomValue()

