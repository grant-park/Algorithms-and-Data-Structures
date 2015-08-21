class Quicksort {

	int[] theArray;
	int length;

	public void sort(int[] inputArray) {
		if (inputArray == null || inputArray.length == 0) {
			return;
		}
		theArray = inputArray;
		length = inputArray.length;
		quicksort(0,length-1);
	}

	public void quicksort(int lowerIndex,int higherIndex) {
		int i = lowerIndex;
		int j = higherIndex;
		int pivot = theArray[lowerIndex + (higherIndex-lowerIndex)/2];
		while (i<=j) {
			while (theArray[i]<pivot) {
				i++;
			}
			while (theArray[j]>pivot) {
				j--;
			}
			if (i <= j) {
				switching(i,j);
				i++;
				j--;
			}
		}
		if (lowerIndex<j) {
			quicksort(lowerIndex,j);
		}
		if (higherIndex>i) {
			quicksort(i,higherIndex);
		}
	}

	public void switching(int i,int j) {
		int temp = theArray[i];
		theArray[i] = theArray[j];
		theArray[j] = temp;
	}

	public static void main(String args[]) {
		Quicksort sorter = new Quicksort();
		int[] test = {2,1,6,8,4,8,0,-1,-2};
		sorter.sort(test);
		for (int i:test) {
			System.out.print(i);
			System.out.print(" ");
		}
	}

}