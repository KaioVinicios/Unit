function LinkedList() {
    var Node = function(element) {
        this.element = element
        this.next = null
    }

    var length = 0
    var head = null

    this.addCustomer = function(element) {
        var node = new Node(element),current
        if(head === null){
            head = node
        }
        else {
            current = head 

            while (current.next) {
                current = current.next
            }
            current.next = node
        }
        length++ 
    }

    
    this.removeNextCustomer = function(position) {
        if (position > -1 && position < length) {
            var current = head, previous, index = 0
            if (position === 0) {
                head = current.next
            } else {
                while (index++ < position) {
                    previous = current
                    current = current.next
                }
                previous.next = current.next
            }
            length--
            return current.element
        } else {
            return null
        }
    }

    this.toString = function() {
        var current = head, string = ''
        while (current) {
            string += current.element + ' '
            current = current.next
        }
        return string
    }

    this.listCustomers = function() {
        console.log(this.toString())
    }
}


// Teste

var li = new LinkedList()
li.addCustomer('1')
li.addCustomer('2')
li.addCustomer('3')
li.removeNextCustomer(0)
li.listCustomers()
