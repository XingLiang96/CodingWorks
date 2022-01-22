#include<iostream>
#define MAX 1000
using namespace std;

//the main menu
void showMenu() {

	cout << "************************************" << endl;
	cout << "*****	1. Add a Contact       *****" << endl;
	cout << "*****	2. Show All Contacts   *****" << endl;
	cout << "*****	3. Delete a Contact    *****" << endl;
	cout << "*****	4. Search a Contact    *****" << endl;
	cout << "*****	5. Modify a Contact    *****" << endl;
	cout << "*****	6. Delete All Contacts *****" << endl;
	cout << "*****	0. Exit This System    *****" << endl;
	cout << "************************************" << endl;

}

//the information of an individual
struct Person {

	string name;
	int sex;  //1-male  2- female
	int age;
	string phoneNum;
	string postcode;

};

//the contact book, maximum is 1000 contacts
struct Addressbook {

	struct Person personArr[MAX];
	int size;

};

//add a person
void addPerson(Addressbook* book) {

	cout << "Enter the Name: ";
	cin >> book->personArr[book->size].name;
	cout << "Enter Gender (1-male  2- female): ";
	cin >> book->personArr[book->size].sex;
	cout << "Enter the Age: ";
	cin >> book->personArr[book->size].age;
	cout << "Enter phone number: ";
	cin >> book->personArr[book->size].phoneNum;
	cout << "Enter Postcode: ";
	cin >> book->personArr[book->size].postcode;
	cout << "Done!" << endl;

	book->size++;  //

	system("pause");
	system("cls");

}

void showPerson(Addressbook book) {
	//check is there any contact?
	if (book.size == 0) {

		cout << "No Any Contact" << endl;

	}
	else {
		//show all contacts
		for (int i = 0; i < book.size; i++) {
			cout << "Name:" << book.personArr[i].name << "\t";
			cout << "Gender:" << (book.personArr[i].sex == 1 ? "Male" : "Female") << "\t";
			cout << "Age:" << book.personArr[i].age << "\t";
			cout << "Phone Num:" << book.personArr[i].phoneNum << "\t";
			cout << "Postcode:" << book.personArr[i].postcode << endl;
		}
	}
	system("pause");
	system("cls");
}

//to check is a person existed
int is_exist(Addressbook* book, string name_delete)
{
	for (int i = 0; i < book->size; i++)
	{
		if (book->personArr[i].name == name_delete)
		{
			return i;
		}
	}
	return -1;
}

//to delect a person
void deletePerson(Addressbook* book, string name_delete) {

	// call the is_exist function, is the name is exist return the location in the array... if not exist return -1

	int ret = is_exist(book, name_delete);
	if (ret == -1)
	{
		cout << "This person is not existed in your contacts!" << endl;
	}
	else
	{
		int i = ret;
		cout << "Do you want to delect the person shown below? (1-Delete  2-Cancel)" << endl;
		cout << "Name:" << book->personArr[i].name << "\t";
		cout << "Gender:" << (book->personArr[i].sex == 1 ? "Male" : "Female") << "\t";
		cout << "Age:" << book->personArr[i].age << "\t";
		cout << "Phone Num:" << book->personArr[i].phoneNum << "\t";
		cout << "Postcode:" << book->personArr[i].postcode << endl;
		int isDelete;
		cin >> isDelete;

		if (isDelete == 1)
		{
			for (int i = ret; i < book->size; i++)
			{
				// move all the contacts, behind the delect person, 1 position forwards in the array
				// i is the delect one, replaced by the later one 
				book->personArr[i] = book->personArr[i + 1];
				cout << "Deleted!" << endl;
				book->size--;

			}

		}
		else
		{
			cout << "You've canceled the delete process successfully!" << endl;

		}

	}

	system("pause");
	system("cls");

}

void nameSearch(Addressbook book, string name_search) {

	int ret = is_exist(&book, name_search);
	if (ret == -1)
	{
		cout << "This person is not in your contacts!" << endl;
	}
	else
	{
		int i = ret;
		cout << "The person you search is shown in following: " << endl;
		cout << "Name:" << book.personArr[i].name << "\t";
		cout << "Gender:" << (book.personArr[i].sex == 1 ? "Male" : "Female") << "\t";
		cout << "Age:" << book.personArr[i].age << "\t";
		cout << "Phone Num:" << book.personArr[i].phoneNum << "\t";
		cout << "Postcode:" << book.personArr[i].postcode << endl;
	}

	system("pause");
	system("cls");
}


int main() {

	Addressbook book;
	book.size = 0;

	int userInput;  //input number

	// loop until input "0" to exit
	while (true) {

		showMenu();

		cin >> userInput;

		switch (userInput) {

		case 1:  //1. Add a Contact
			addPerson(&book);  //book is a variable to save the 5 info of each contact
			break;

		case 2:  //2. Show All Contacts
			showPerson(book);
			break;

		case 3:  //3. Delete a Contact
		{
			//search name to check whether the contact is in the addressbook
			cout << "Enter a name you want to delect: ";
			string name_delete;
			cin >> name_delete;

			//delect the selected person
			deletePerson(&book, name_delete);

			//multiple codings inside the switch statement should be contained by {}
		}
		break;
		
		case 4:  //4. Search a Contact
		{
			cout << "Please enter the name you want to search: ";
			string name_search;
			cin >> name_search;
			nameSearch(book, name_search);
		}

		break;

		case 5:  //5. Modify a Contact
			break;

		case 6:  //6. Delete All Contacts
			break;

		case 0:  //0. Exit This System
			cout << "See you next time!" << endl;
			system("pause");  //任意按键继续
			return 0;
			break;

		default:
			break;

		}
	}



	system("pause");  //任意按键继续

	return 0;

}