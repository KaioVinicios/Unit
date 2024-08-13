/* ex01
var avgTempJan = 31.9
var avgTempFev = 35.3
var avgTempMar = 42
var avgTempApr = 38
var avgTempMay = 25.5

console.log('Temp: ' + avgTempApr)

ex02
var avgTemp = [31.9, 35.0, 3, 31]
console.log('Temp: ' + avgTemp[0])


ex03
var daysOfWeek = new Array(7)
daysOfWeek[0] = 'Domingo'

console.log(daysOfWeek.length) 

var daysOfWeek = new Array('D', 'S', 'T', 'Q', 'QI', 'S', 'SA')
console.log(daysOfWeek.length)
console.log(daysOfWeek[3])

for(let i = 0; i < daysOfWeek.length; i ++){
    console.log(daysOfWeek[i])
}
*/

var numbers = [0,1,2,3,4,5,6,7,8,9]
console.log(numbers)

numbers[numbers.length] = 10
numbers[numbers.length] = 11

numbers.push(12)
numbers.unshift(-1)
numbers.pop()
numbers.shift()