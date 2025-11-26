#include <stdio.h>

// Funktion zur Ausgabe der Matrix
void printMatrix(int arr[][4], int rows) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < 4; j++) {
            printf("%d\t", arr[i][j]);
        }
        printf("\n");
    }
}

// b) Summe der Hauptdiagonale berechnen
int calculateDiagonalSum(int arr[][4], int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i][i];
    }
    return sum;
}

// Hilfsfunktion: Prüfen, ob eine Zahl prim ist
int isPrime(int n) {
    if (n < 2) return 0;
    for (int i = 2; i*i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main() {
    int matrix[4][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12},
        {13, 14, 15, 16}
    };

    printf("Originalmatrix:\n");
    printMatrix(matrix, 4);

    // b) Summe der Hauptdiagonale
    int diagSum = calculateDiagonalSum(matrix, 4);
    printf("\nSumme der Hauptdiagonale: %d\n", diagSum);

    // c) Alle geraden Zahlen durch 0 ersetzen
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (matrix[i][j] % 2 == 0) {
                matrix[i][j] = 0;
            }
        }
    }

    printf("\nMatrix nach Ersetzen der geraden Zahlen durch 0:\n");
    printMatrix(matrix, 4);

    // d) Alle Primzahlen durch 0 ersetzen
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (isPrime(matrix[i][j])) {
                matrix[i][j] = 0;
            }
        }
    }

    printf("\nMatrix nach Ersetzen der Primzahlendurch 0:\n");
    printMatrix(matrix, 4);

    return 0;
}
