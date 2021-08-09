package main

import (
  "fmt"
  "log"
  "github.com/mattn/go-pipeline"
  "os"
)

func main() {
  contest := os.Args[1]
  task := os.Args[2]

  file_name := contest+"/"+task+".go"
  out, err := pipeline.Output(
    []string{"cat", "data"},
    []string{"go", "run", file_name},
  )

  if err != nil {
      log.Fatal(err)
  }

  fmt.Println(string(out))
}