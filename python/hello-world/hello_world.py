def hello():
    try:
      return("Hello, World!")
    except AssertionError as Err:
      return(Err.message)
