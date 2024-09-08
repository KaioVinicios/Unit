function areDelimitersBalanced(expression) {
    const stack = [];
    const pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    };

    for (let char of expression) {
        if (['(', '[', '{'].includes(char)) {
            stack.push(char);
        } else if ([')', ']', '}'].includes(char)) {
            if (stack.length === 0 || stack.pop() !== pairs[char]) {
                return false;
            }
        }
    }

    return stack.length === 0;
}

console.log(areDelimitersBalanced("(){}[]")); 
console.log(areDelimitersBalanced("({[]})")); 
console.log(areDelimitersBalanced("({[})]")); 
console.log(areDelimitersBalanced("{[(])}")); 
console.log(areDelimitersBalanced("({[(){}]})")); 