
console.log(3 > 2 > 1);
console.log(3 < 2 < 1);

const email = prompt("email");

const emaillen = (email.length);

console.log(emaillen);

const dotindex = email.lastIndexOf(".");
console.log(dotindex);
const atindex = email.lastIndexOf("@");

if (emaillen < 11 || ((emaillen - 1) - dotindex) < 2 || dotindex - atindex < 3) { console.log("not valid"); }
else { console.log("valid"); }

if (true)  {
    console.log('hello');
}
