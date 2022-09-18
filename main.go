package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"log"
	"net/http"

	_ "github.com/lib/pq"
)

const (
	host     = "localhost"
	port     = 5432
	user     = "postgres"
	password = "Mhnina3ideqea!"
	dbname   = "tabula"
)

type User struct {
	ID        int    `json:"id"`
	Email     string `json:"email"`
	FirstName string `json:"first_name"`
	LastName  string `json:"last_name"`
	Gender    string `json:"gender"`
	Type      string `json:"type"`
}

func main() {
	mux := http.NewServeMux()

	mux.HandleFunc("/addUser", addUser)
	mux.HandleFunc("/getUser", getOneUser)
	mux.HandleFunc("/getStudents", getAllStudents)

	fmt.Printf("Starting server at port 4000\n")
	err := http.ListenAndServe(":4000", mux)

	log.Fatal(err)
}

func connectToDB() *sql.DB {
	psqlConnect := fmt.Sprintf("host=%s port=%d user=%s password=%s dbname=%s sslmode=disable", host, port, user, password, dbname)

	db, err := sql.Open("postgres", psqlConnect)
	if err != nil {
		panic(err)
	}

	fmt.Println("Successfuly connected!")

	return db
}

// add users
func addUser(w http.ResponseWriter, r *http.Request) {
	db := connectToDB()
	defer db.Close()

	var user User
	err := json.NewDecoder(r.Body).Decode(&user)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	fmt.Printf("%+v\n", user)

	sqlStatement := `
	INSERT INTO users (first_name, last_name, email, gender, type)
	VALUES ($1, $2, $3, $4, $5)
	RETURNING id
	`

	id := 0
	err = db.QueryRow(sqlStatement, user.FirstName, user.LastName, user.Email, user.Gender, user.Type).Scan(&id)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	w.WriteHeader(200)
}

func getAllStudents(w http.ResponseWriter, r *http.Request) {
	db := connectToDB()
	defer db.Close()

	var users []User

	sqlStatement := `SELECT * FROM users WHERE type = 'student'`

	result, err := db.Query(sqlStatement)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
	defer result.Close()
	for result.Next() {
		var user User
		err := result.Scan(&user.ID, &user.Email, &user.FirstName, &user.LastName, &user.Gender, &user.Type)
		if err != nil {
			fmt.Println(err)
		}

		users = append(users, user)
	}

	err = result.Err()
	if err != nil {
		fmt.Println(err)
	}

	response, err := json.Marshal(users)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.Write(response)
}

func getOneUser(w http.ResponseWriter, r *http.Request) {
	db := connectToDB()
	defer db.Close()

	var user User
	id := r.URL.Query().Get("id")
	fmt.Println(id)

	sqlStatement := `SELECT * FROM users WHERE id = $1;`

	row := db.QueryRow(sqlStatement, id)
	err := row.Scan(&user.ID, &user.Email, &user.FirstName, &user.LastName, &user.Gender, &user.Type)

	// This should be handled better, with multiple error types
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	response, err := json.Marshal(user)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.Write(response)
}
