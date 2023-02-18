library(tidyverse)
library(tidytext)
library(gutenbergr)

raj_raw <- gutenberg_download(1513, meta_fields = "title")

head(raj_raw)

# clean data
raj = raj_raw %>%
  # The actual book doesn't start until line 96
  slice(96:n()) %>% 
  # Get rid of rows where text is missing
  drop_na(text) %>% 
  # Chapters start with CHAPTER X, 
  # so mark if each row is a chapter start
  # cumsum() calculates the cumulative sum, 
  # so it'll increase every time there's
  # a new chapter and automatically make chapter numbers
  mutate(chapter_start = str_detect(text, "^CHAPTER"),
         chapter_number = cumsum(chapter_start)) %>% 
  # Get rid of these columns
  select(-gutenberg_id, -title, -chapter_start)

head(raj)

raj_words <- raj_raw %>% 
  drop_na(text) %>% 
  unnest_tokens(word, text)

head(raj_words)

top_words_raj <- raj_words %>% 
  # Remove stop words
  anti_join(stop_words) %>% 
  # Get rid of old timey words and stage directions
  filter(!(word %in% c("thou", "thy", "haue", "thee", 
                       "thine", "enter", "exeunt", "exit"))) %>% 
  # Count all the words in each play
  count(title, word, sort = TRUE) %>% 
  # Keep top 15 in each play
  group_by(title) %>% 
  top_n(15) %>% 
  ungroup() %>% 
  # Make the words an ordered factor so they plot in order
  mutate(word = fct_inorder(word))

top_words_raj

ggplot(top_words_raj, aes(y = fct_rev(word), x = n, fill = title)) + 
  geom_col() + 
  guides(fill = FALSE) +
  labs(y = "Count", x = NULL, 
       title = "15 most frequent words in four Shakespearean tragedies") +
  facet_wrap(vars(title), scales = "free_y") +
  theme_bw()