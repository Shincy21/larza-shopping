#include <stdio.h>
#include <string.h>


struct LodgeBill {
    char guestName[100];
    char checkInDate[12];
    char checkOutDate[12];
    int roomNumber;
    double roomCharge;
    double extraServices;
    double totalAmount;
};


double calculateTotalAmount(double roomCharge, double extraServices) {
    return roomCharge + extraServices;
}

int main() {
    struct LodgeBill bill;
    printf("Annapurna Hotel Lodge Bill\n");
    printf("Guest Name: ");
    fgets(bill.guestName, sizeof(bill.guestName), stdin);
    printf("Check-in Date: ");
    fgets(bill.checkInDate, sizeof(bill.checkInDate), stdin);
    printf("Check-out Date: ");
    fgets(bill.checkOutDate, sizeof(bill.checkOutDate), stdin);
    printf("Room Number: ");
    scanf("%d", &bill.roomNumber);
    printf("Room Charge (per night): ");
    scanf("%lf", &bill.roomCharge);
    printf("Extra Services Charge: ");
    scanf("%lf", &bill.extraServices);

    
    bill.totalAmount = calculateTotalAmount(bill.roomCharge, bill.extraServices);

    // Print the lodge bill
    printf("\n--- Annapurna Hotel Lodge Bill ---\n");
    printf("Guest Name: %s", bill.guestName);
    printf("Check-in Date: %s", bill.checkInDate);
    printf("Check-out Date: %s", bill.checkOutDate);
    printf("Room Number: %d\n", bill.roomNumber);
    printf("Room Charge (per night): %.2lf\n", bill.roomCharge);
    printf("Extra Services Charge: %.2lf\n", bill.extraServices);
    printf("Total Amount: %.2lf\n", bill.totalAmount);

    return 0;
}
