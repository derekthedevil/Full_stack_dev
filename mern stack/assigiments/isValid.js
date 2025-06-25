
function isValidIdentifier(identifier){
    if (48 >= identifier.charCodeAt(1) <= 57) {
        ans = "True"
    }
    console.log(ans);
}

isValidIdentifier("myVariable"); // Logs: myVariable is a valid identifier.
isValidIdentifier("123abc"); // Logs: 123abc is not a valid identifier.
isValidIdentifier("_pr&ivate"); // Logs: _pr&ivate is not a valid identifier.


