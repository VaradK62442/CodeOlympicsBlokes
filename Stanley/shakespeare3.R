library(tidyverse)

word_freq_data = read.csv("wordFreq.csv")
first_50 = head(word_freq_data, 50)

ggplot(first_50, aes(x=word, y=count)) + 
  geom_bar(stat="identity")
