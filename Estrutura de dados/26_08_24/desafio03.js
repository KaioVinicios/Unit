function Stack() {
    var items = []

    this.push = function(element) { 
        items.push(element)
    }

    this.pop = function() {
        return items.pop()
    }

    this.peek = function() {
        return items[items.length - 1]
    }

    this.isEmpty = function() {
        return items.length === 0
    }

    this.clear = function() {
        items = []
    }

    this.size = function() {
        return items.length
    }

    this.print = function() {
        console.log(items)
    }

    this.getItems = function() {
        return items
    }
}

function isPalindrome(string) {
    let stack = new Stack();
    let cleanedString = string.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();

    for (let i = 0; i < cleanedString.length; i++) {
        stack.push(cleanedString[i]);
    }

    for (let i = 0; i < cleanedString.length; i++) {
        if (cleanedString[i] !== stack.pop()) {
            return false;
        }
    }

    return true;
}

console.log(isPalindrome("radar"));
console.log(isPalindrome("hello"));
console.log(isPalindrome("A man, a plan, a canal, Panama"));