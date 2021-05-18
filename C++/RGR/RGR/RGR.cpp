#include <iostream>
#include <cstdlib>
#include <string>
#include <locale>
#include <cmath>

using namespace std;

class s9
{
public:

	void set_numbers(int &num11, int &num22)
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
		num11 = to_ninefold(ch1);
		num22 = to_ninefold(ch2);
	}
	
	string plus(int first, int second)
	{
		int temp, sum;
		ans = 1;
		temp =  0;
		while (first)
		{
			ans *= 10;
			sum = first % 10 + second % 10 + temp;
			if (sum >= 9)
			{
				ans += (sum) % 9;
				temp = (sum) / 9; 
			}
			else
			{
				ans += sum;
				if (temp != 0)
					temp = 0;
			}
			first /= 10;
			second /= 10;
		}
		return to_string(to_tenfold(reverse(ans)));
	}
	string minus(int first, int second)
	{
		ans = 1;
		bool nonary = false; //занят ли "десяток" в следующей цифре
		bool temp = false; //занято ли "десяток" в текущей цифре

		while (first > 0)
		{
			if (nonary)
				temp = true;

			if ((first % 10) - (second % 10) <= 0)
			{
				nonary = true;
				ans = ans * 10 + ((nonary * 9 - temp) + (first % 10) - (second % 10));
			}
			else
			{
				nonary = false;
				ans = ans * 10 + (first % 10 - temp) - (second % 10);

			}
			temp = false;
			first /= 10;
			second /= 10;

		}
		return to_string(to_tenfold(reverse(ans)));
	}

private:
	int ch1, ch2, ans;

	int reverse(int num)
	{
		int num_new = 0;
		while (num)
		{
			num_new = num_new * 10 + num % 10;
			num /= 10;
		}
		return num_new/10;
	}
	int to_ninefold(int num)
	{
		int num_new = 1;
		while (num > 8)
		{
			num_new = num_new * 10 + (num % 9);
			num /= 9;
		}
		num = num_new * 10 + num;
		num = reverse(num);
		return num;
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
	int num1, num2;
	setlocale(LC_ALL, "rus");
	cout << "Оборожный Данил Сергеевич\nИС-29\nНапишите класс s9, выполняющий сложение и вычитание двух чисел в системе счисления 9. Из большего числа должно вычитаться меньшее. Заранее не известно, какое число больше." << endl;
	check.set_numbers(num1, num2);
	cout << "Plus: ";
	cout << check.plus(num1, num2) << endl;
	cout << "Minus: ";
	cout << check.minus(num1, num2) << endl;
	system("pause");
	return 0;
}