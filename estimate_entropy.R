require(dplyr)
estimate_entropy <- function(counts) {
  
  thoth_entropy <- system2("/usr/local/var/pyenv/versions/2.7.12/bin/python", 
                           args = c("thoth_entropy.py", sprintf('%i',counts)),
                           stdout = TRUE) %>%
    sub("\\[ ", "", .) %>%
    sub("\\]", "", .) %>%
    strsplit("  ") %>%
    unlist %>%
    as.numeric
  
  data.frame(t(thoth_entropy))
  names(thoth_entropy) <- c("mean", "lower_sd", "upper_sd", "lower_2sd", "upper_2sd")
  
  return(thoth_entropy)
  
}