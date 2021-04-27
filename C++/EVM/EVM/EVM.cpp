#include <iostream>
#include <cstdlib>
#include <string>  

using namespace std;


bool intSigned(const string& s)
{
	for (int i = 0; i < s.length(); i++) {
		if (s[i] >= 'a' && s[i] <= 'z')
		{
			return false;
		}
	}
	return true;
}//проверка строки на наличие отличных от цифр символов

int main()
{
	string resist[6];
	double a1, a2, d1, d2, c1, c2; 
	double result;
	setlocale(LC_ALL, "Russian");
	cout << "Выполнил работу: " << "Оборожный Данил Сергеевич\n";
	cout << "Группа: " << "ИС-29\n";
	cout << "Задание: "
		<< "Определить сопротивление участка цепи A-B\n";
	cout << "СХЕМА ПСЕВДО-ГРАФИКОЙ\n";
	cout << "   |---A1--D1--C1---|\n"
		 << "A--|    |-----|     |--B\n"
		 << "   |---A2--D2--C2---|\n";
	cout << "Введите сопротивления элементов a1, a2, d1, d2, c1, c2 согласно схеме выше" << endl;
	setlocale(LC_ALL, "English");

	cin >> resist[0] >> resist[1] >> resist[2] >> resist[3] >> resist[4] >> resist[5];
	
	for (int i = 0; i < 6; i++)
	{
		if (!intSigned(resist[i]))
		{
			cout << "Invalid input: " << resist[i] << endl;
			return 0;
		}

	}
	a1 = atof(resist[0].c_str());
	a2 = atof(resist[1].c_str());
	c1 = atof(resist[4].c_str());
	c2 = atof(resist[5].c_str());

	cout << "Total resistance: ";
	result = ((a1 * a2) / (a1 + a2)) + ((c1 * c2) / (c1 + c2));

	cout << result << endl;
	system("PAUSE");
	return 0;
}