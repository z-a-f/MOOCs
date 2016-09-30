#ifndef ROT_HPP
#define ROT_HPP

#include <string>

char rotE (char m, std::size_t k) {
  if (m >= 'a' && m <= 'z')
    return ((m - 'a') + k) % 26 + 'a';
  else
    return m;
}

char rotE (char m, char k) {
  return rotE (m, std::size_t(k-'a'));
}

std::string rotE (std::string m, std::size_t k) {
  std::string c = "";
  for (std::size_t i = 0; i < m.length(); i++) {
    c += rotE(m[i], k);
  }
  return c;
}

std::string rotE (std::string m, char k) {
  return rotE (m, std::size_t(k-'a'));
}


/** **/
std::string rot (std::string m, std::size_t k, bool decodeMode) {
  if (decodeMode) {
    return rotE(m, 26 - k);
  } else {
    return rotE(m, k);
  }
}

std::string rot (std::string m, char k, bool decodeMode) {
  return rot(m, std::size_t(k - 'a'), decodeMode);
}

#endif
