class Quicksort {
    var theArray: [Int] = []
    func switching(first: Int, second: Int) {
        var temp = theArray[first]
        theArray[first] = theArray[second]
        theArray[second] = temp
    }
    func quicksort(lowerIndex: Int, higherIndex: Int) {
        var i: Int = lowerIndex
        var j: Int = higherIndex
        var pivot: Int = theArray[lowerIndex + (higherIndex - lowerIndex)/2]
        while i<=j {
            while theArray[i]<pivot {
                i++
            }
            while theArray[j]>pivot {
                j--
            }
            if i<=j {
                switching(i,second: j)
            }
        }
        if lowerIndex<j {
            quicksort(lowerIndex, higherIndex: j)
        }
        if higherIndex > i {
            quicksort(i, higherIndex: higherIndex)
        }
    }
    func sort(inputArray: [Int]) {
        if inputArray.count == 0 {
            return
        }
        quicksort(0,higherIndex: inputArray.count-1)
    }
}