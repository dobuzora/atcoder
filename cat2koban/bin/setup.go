package main

import (
  "os"
  "os/exec"
  "log"
)

func main() {
  contest := os.Args[1]
  task := os.Args[2]
  mkdir := exec.Command("mkdir", contest)
  cp := exec.Command("cp", "template.go", contest+"/"+task+".go")
  err_mkdir := mkdir.Run()
  if err_mkdir != nil {
		log.Fatal(err_mkdir)
	}
  err_cp := cp.Run()
  if err_cp != nil {
		log.Fatal(err_cp)
	}
}
