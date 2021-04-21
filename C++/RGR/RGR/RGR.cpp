#include <iostream>
#include <cstdlib>
#include <string>
#include <locale>
#include <cmath>

using namespace std;

class s9
{
public:

	void set_numbers()
	{
		string first, second;

		while (((intSigned(first) == false) || (intSigned(second) == false)) || ((first == "") && (second == "")))//проверка корректности вводимых данных, работает до тех пор пока пользователь не введёт числа
		{
			cout << "Введите 2 целых числа" << endl;
			cin >> first >> second;
		}
		ch1 = stoi(first);
		ch2 = stoi(second);
		if (ch1 < ch2)//изначально считается, что ch1 > ch2, иначе обмен
		{
			swap(ch2, ch1);
		}
		ch1 = to_ninefold(ch1);
		ch2 = to_ninefold(ch2);
	}
	
	string plus()
	{
		ans = ch1 + ch2;
		cout << "Plus: ";
		return to_string(to_tenfold(ans));
	}
	string minus()
	{
		ans = ch1 - ch2;
		cout << "Minus: ";
		return to_string(to_tenfold(ans));
	}

private:
	int ch1, ch2, ans;

	int to_ninefold(int num)
	{
		int num_new = 0;
		while (num > 8)
		{
			num_new = num_new * 10 + num % 9;
			num /= 9;
		}
		num = num_new * 10 + num;
		num_new = 0;
		while (num)
		{
			num_new = num_new * 10 + num % 10;
			num /= 10;
		}
		return num_new;
	}//конвертирование в 9ю СС
	int to_tenfold(int num)
	{
		int num_new, i;
		num_new = i = 0;
		while (num > 0)
		{
			num_new = num_new + (num % 10) * pow(9, i);
			num /= 10;
			i++;
		}
		return num_new;
	}//конвертирование в 10ю СС
	bool intSigned(const string& s)
	{
		for (int i = 0; i < s.length(); i++) {
			if (s[i] >= 'a' && s[i] <= 'z')
			{
				cout << "Не верный формат исходных данных" << endl;
				return false;
			}
		}
		return true;
	}//проверка строки на наличие отличных от цифр символов
};


int main()
{
	s9 check;
	setlocale(LC_ALL, "rus");
	cout << "Оборожный Данил Сергеевич\n" << "ИС-29\n" << "Напишите класс s9, выполняющий сложение и вычитание двух чисел в системе счисления 9. Из большего числа должно вычитаться меньшее. Заранее не известно, какое число больше." << endl;
	check.set_numbers();
	cout << check.plus() << endl;
	cout << check.minus() << endl;
	system("pause");
	return 0;
}