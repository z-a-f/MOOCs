#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int hex2int(const string& hex) {
  int out = 0;
  for (unsigned int i = 0; i < hex.length(); i++) {
    if (hex[i] >= '0' && hex[i] <= '9') {
      out = (out << 4) + int(hex[i] - '0');
    } else if (hex[i] >= 'a' && hex[i] <= 'f') {
      out = (out << 4) + int(hex[i] - 'a') + 10;
    } else if (hex[i] >= 'A' && hex[i] <= 'F') {
      out = (out << 4) + int (hex[i] - 'A') + 10;
    } else {
      return out;
    }
  }
  return out;
}

// Method to read the characters:
vector<int> readCypher (const string& fName) {
  string cypherText = "aa";	// Just a dummy to set the initial size
  int i = 0;
  vector<int> out;
  ifstream inFile;
  inFile.open(fName);
  while (inFile.get(cypherText.at(i))) {
    // cout << cypherText.at(i);
    if (i == 1) {
      // cout << cypherText << ' ';
      // cout << hex2int(cypherText) << endl;
      out.push_back(hex2int(cypherText));
      // cout << cypherText << endl;
      // cout << out.back() << endl;
    }
    i = 1-i;
    
  }
  inFile.close();
  return out;
}

vector<int> freq(const vector<int>& V, const int& step) {
  vector<int> out;
  out.resize(256);
  for (size_t i = 0; i < V.size(); i += step) {
    out.at(V.at(i)) += 1;
  }
  return out;
}

int findKeyLength(const vector<int>& cVector, int maxLength) {
  vector< vector<int> > distrib;
  int min = 256;
  int keyLength = 0;
  cout << "Checking keys: " << endl;

  for (int i = 1; i <= maxLength; i++) {
    distrib.push_back(freq(cVector, i));
  }
  int k = 0;
  for (vector< vector<int> >::iterator i = distrib.begin(); i != distrib.end(); ++i) {
    float sum = 0.0;
    k++;
    for (vector<int>::iterator j = i->begin(); j != i->end(); ++j) {
      sum += (*j == 0) ? 0 : (1.0 / *j)*(1.0 / *j);
    }
    if (sum < min) {
      keyLength = k;
      min = sum;
    }
    cout << k << ": " << sum << endl;
  }

  cout << "Assuming key length = " << keyLength << endl;
  return keyLength;
}

vector<int> findKey(vector<int> C, int len) {
  vector<int> key;
  int max = 0;
  int k;
  key.resize(256);
  for (int i = 1; i <= len; i++) {
    vector<int> distrib;
    for (size_t j = i-1; j < C.size(); j+=len) {
      distrib.at(C.at(j))++;
    }
    for (size_t j = 0; j <= distrib.size(); j++) {
      if (distrib.at(j) > max) {
	max = distrib.at(j);
	k = int(j);
      }
    }
    key.push_back(k);
  }
  return key;
}


int main() {
  vector<int> cVector = readCypher ("cypher.txt");
  /*
  cout << cVector.size() << endl;
  for (vector<int>::iterator i = cVector.begin(); i != cVector.end(); ++i) {
    cout << *i << ' ';
    printf("%X\n", *i);
  }
  */
  int keyLen;
  keyLen = findKeyLength(cVector, 13);
  vector<int> key = findKey(cVector, keyLen);
  
}

