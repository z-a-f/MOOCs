#ifndef VIGENERE_HPP
#define VIGENERE_HPP

#include <string>

#include "Rot.hpp"

/* If decode mode is given the modular vigener is used.
 * The decode mode specifies if currently decoding
 */

std::string vigenere (std::string m, std::string k, bool decodeMode) {
  std::size_t len = m.length(); // (m.length() > k.length()) ? m.length() : k.length();
  std::string c = "";
  if (decodeMode) {
    for (std::size_t i = 0; i < len; i++) {
      c += rotE(m[i], std::size_t(26-(k[i%k.length()] - 'a')));
    }
  } else {
    for (std::size_t i = 0; i < len; i++) {
      c += rotE(m[i], k[i%k.length()]);
    }
  }
  return c;
}

/* If decode mode is not given the XOR vigenere is used.
 */
std::string vigenere (std::string m, std::string k) {
  std::size_t len = m.length();
  std::string c = "";
  for (std::size_t i = 0; i < len; i++) {
    c+= m[i] ^ k[i%k.length()];
  }
  return c;
}

/*
 * Finding the frequencies for vigenere
 */
#include "englishFrequencies.hpp" // declares ENGLISH_FREQ



#endif
