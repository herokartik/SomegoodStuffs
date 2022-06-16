function power2(n){
    let p=parseInt(Math.log(n)/Math.log(2),10)
    return Math.pow(2,p)
}
let n=33
console.log(power2(n))