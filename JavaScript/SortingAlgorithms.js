//Merge sort

function MergeSort(arr) {

    function _Merged(arr, low, high, mid) {
        let leftArray = arr.slice(low, mid+1)
        let rightArray = arr.slice(mid+1, high+1)
        let k = low
        let i = 0
        let j = 0
        while (i < leftArray.length && j < rightArray.length) {
            if (leftArray[i] <= rightArray[j]) {
                arr[k] = leftArray[i]
                i++;
                k++;
            } else {
                arr[k] = rightArray[j]
                j++;
                k++;
            }
        }

        while (i < leftArray.length) {
            arr[k++] = leftArray[i]
            i++;
        }

        while (j < rightArray.length) {
            arr[k++] = rightArray[j]
            j++;
        }
        return arr;
    }


    function _MergedArray(arr, left, right) {
        if (left < right) {
            let mid = parseInt(left + (right-left) / 2)
            _MergedArray(arr, left, mid);
            _MergedArray(arr, mid+1, right)
            _Merged(arr, left, right, mid)
        }
    }
    return _MergedArray(arr, 0, arr.length-1)
}

let arr = [12, 11, 13, 5, 6, 7];
MergeSort(arr)
console.log("MergedSort ", arr)

let arr1 = [1, 4, -2, 12, 9, -6, 100];
MergeSort(arr1)
console.log("MergedSort ", arr1)

let arr2 = [10, 7, 8, 9, 1, 5, -1];
MergeSort(arr2)
console.log("MergedSort ", arr2)


//Quick sort
function QuickSort(arr) {

    function Partition(arr, left, right) {
        let low = left
        let pivot = arr[right]
        for (let i = left; i < right; i++) {
            if (arr[i] < pivot) {
                let temp = arr[i]
                arr[i] = arr[low]
                arr[low] = temp
                low++;
            }
        }
        arr[right], arr[low] = arr[low], arr[right]
        let temp = arr[right]
        arr[right] = arr[low]
        arr[low] = temp
        return low;
    }

    function _QuickSort(arr, left, right) {
        if (left < right) {
            let pivotIndex = Partition(arr, left, right)
            _QuickSort(arr, left, pivotIndex-1)
            _QuickSort(arr, pivotIndex+1, right)
        }
        return arr;
    }
    return _QuickSort(arr, 0, arr.length-1)
}

let arr3 = [10, 7, 8, 9, 1, 5, -1] 
QuickSort(arr3)
console.log("QuickSort ", arr3)

let arr4 = [12, 11, 13, 5, 6, 7];
QuickSort(arr4)
console.log("QuickSort ", arr4)

let arr5 = [1, 4, -2, 12, 9, -6, 100];
QuickSort(arr5)
console.log("QuickSort ", arr5)
