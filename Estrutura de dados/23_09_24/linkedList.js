function LinkedList() {
    var Node = function(element) {
        this.element = element
        this.next = null
    }

    var length = 0
    var head = null

    this.append = function(element) {
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

    this.insert = function(position, element) {
        if (position >= 0 && position <= length) {
            var node = new Node(element), current = head, previous, index = 0
            if (position === 0) {
                node.next = current
                head = node
            } else {
                while (index++ < position) {
                    previous = current
                    current = current.next
                }
                node.next = current
                previous.next = node
            }
            length++
            return true
        }
        else {
            return false
        }
    }

    this.removeAt = function(position) {
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

    this.remove = function(element) {
        //remove o elemnto element ( o paramentro) não a posição
    }

    this.indexOf = function(element) {
        var current = head, index = 0

        while (current) {
            if(element === current.element){
                return index
            }
            index++
            current = current.next
        }
        return - 1
    }

    this.isEmpty = function() {
        //retorna se esta vazia ou não a instancia
    }

    this.size = function() {
        //retorna o tamanho da instancia
    }

  /*  this.getHead = function() {
        return head
    } */

    this.toString = function() {
        var current = head, string = ''
        while (current) {
            string += current.element + ' '
            current = current.next
        }
        return string
    }

    this.print = function() {
        console.log(this.toString())
    }
}


// Teste01

var li = new LinkedList()
li.append('1')
li.append('2')
li.append('3')
li.removeAt(0)
li.insert(0, '1')
li.print()
console.log(li.indexOf('3'))