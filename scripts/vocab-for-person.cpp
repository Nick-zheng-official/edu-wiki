#include <bits/stdc++.h>
using namespace std;
vector<pair<string, int>> vocab;
int reviewday[] = {1, 2, 3, 5, 7, 14, 30, 60};
int num;
time_t pasttime, nowtime;
fstream ioFile("vocabs.txt");
ofstream oFile("export-vocabs.txt");
void cleanspace(string &tar)
{
	for (int i = 0; i < (int)tar.size(); i++)
	{
		if (tar[i] == ' ')
		{
			tar[i] = '_';
		}
	}
}
string restorespace(string tar)
{
	for (int i = 0; i < (int)tar.size(); i++)
	{
		if (tar[i] == '_')
		{
			tar[i] = ' ';
		}
	}
	return tar;
}
void insertvocabs()
{
	cout << "Please type in target vocabs, ended up with '0'\n";
	while (1)
	{
		string tmpvocab;
		cin.ignore();
		getline(cin, tmpvocab);
		if (tmpvocab == "0")
		{
			return;
		}
		else if (tmpvocab == "" || !((tmpvocab[0] >= 'A' && tmpvocab[0] <= 'Z') || (tmpvocab[0] >= 'a' && tmpvocab[0] <= 'z')))
		{
			continue;
		}
		cleanspace(tmpvocab);
		vocab.push_back({tmpvocab, 1});
	}
}
void exportvocabs()
{
	oFile.close();
	oFile.open("export-vocabs.txt");
	for (auto i : vocab)
	{
		if (binary_search(reviewday, reviewday + 8, i.second))
		{
			oFile << restorespace(i.first) << endl;
		}
	}
}
void updgaps()
{
	nowtime = time(0);
	int diff = difftime(nowtime, pasttime) / 86400;
	for (auto &i : vocab)
	{
		i.second += diff;
	}
	pasttime = nowtime;
}
void init()
{
	ioFile >> pasttime >> num;
	for (int i = 1; i <= num; i++)
	{
		string tmpvocab;
		int tmpgap;
		ioFile >> tmpvocab >> tmpgap;
		vocab.push_back({tmpvocab, tmpgap});
	}
	updgaps();
}
void rebuild()
{
	ioFile.close();
	ioFile.open("vocabs.txt", ios::out | ios::trunc);
	ioFile << nowtime << endl
		   << (int)vocab.size() << endl;
	for (auto i : vocab)
	{
		ioFile << i.first << ' ' << i.second << endl;
	}
}
int main()
{
	init();
	cout << "Hello! \n";
	while (1)
	{
		cout << "Please choose from options below: \n 1. insert vocabularies \n 2. export vocabularies that meet deadlines \n 3. stop operating \n";
		int opt;
		cin >> opt;
		if (opt == 1)
		{
			insertvocabs();
			cout << "Done. \n";
		}
		else if (opt == 2)
		{
			exportvocabs();
			cout << "Done. \n";
		}
		else if (opt == 3)
		{
			cout << "ARE YOU SURE TO LEAVE? (y/n)\n";
			char leaveopt;
			cin >> leaveopt;
			if (leaveopt == 'y')
			{
				cout << "Vocabs are automatically exported. Bye! \n";
				exportvocabs();
				rebuild();
				return 0;
			}
			else
			{
				cout << "Cancelled. \n";
			}
		}
		else
		{
			cerr << "Error! \n";
		}
	}
	exportvocabs();
	rebuild();
	return 0;
}
