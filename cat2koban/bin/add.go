package main

import (
  "os"
  "os/exec"
  "log"
)

func main() {
  contest_number := os.Args[1]
  task_type := os.Args[2]
  cmd_mkdir := exec.Command("mkdir", contest_number)
  cmd_cp := exec.Command("cp", "template.go", contest_number+"/"+task_type+".go")
  err_mkdir := cmd_mkdir.Run()
  if err_mkdir != nil {
		log.Fatal(err_mkdir)
	}
  err_cp := cmd_cp.Run()
  if err_cp != nil {
		log.Fatal(err_cp)
	}
}
