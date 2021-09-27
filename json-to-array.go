package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

type NewArticles struct {
	Articles []Article `json:"articles"`
}

type OldArticles struct {
	Articles []Article `json:"articles"`
}

type Article struct {
	ID int `json:"id"`
	Title string `json:"title"`
}

type IDs struct {
	OldID string
	NewID string
}

func main() {
	articles := map[string]IDs{}

	oldFile, err := os.Open("./Input/OldResourceCenter.json")
	if err != nil {
		panic(err)
	}
	defer oldFile.Close()
	data, _ := ioutil.ReadAll(oldFile)
	oldArticles := OldArticles{}
	err = json.Unmarshal(data, &oldArticles)

	for _, v := range(oldArticles.Articles) {
		articles[v.Title] = IDs{OldID: "\"" + strconv.Itoa(v.ID) + "\""}
	}

	newFile, err := os.Open("./Input/NewResourceCenter.json")
	if err != nil {
		panic(err)
	}
	defer newFile.Close()
	data, _ = ioutil.ReadAll(newFile)
	newArticles := NewArticles{}
	err = json.Unmarshal(data, &newArticles)

	for _, v := range(newArticles.Articles) {
		articles[v.Title] = IDs{
			OldID: articles[v.Title].OldID,
			NewID: "\"" + strconv.Itoa(v.ID) + "\"",
		}
	}

	newIDs := []string{}
	oldIDs := []string{}
	unmatchedArticles := []IDs{}

	for _, v := range(articles) {
		if v.NewID == "" || v.OldID == "" {
			unmatchedArticles = append(unmatchedArticles, IDs{OldID: v.OldID, NewID: v.NewID})
			continue
		}
		oldIDs = append(oldIDs, v.OldID)
		newIDs = append(newIDs, v.NewID)	
	}
	oldOutput := "[" + strings.Join(oldIDs, ", ") + "]"
	fmt.Printf("JS formatted array of old IDs:\n\n%s\n\n", oldOutput)
	newOutput := "[" + strings.Join(newIDs, ", ") + "]"
	fmt.Printf("JS formatted array of new IDs:\n\n%s\n\n", newOutput)
	fmt.Println("Unmatched IDs:");
	for _, v := range(unmatchedArticles) {
		fmt.Printf("%+v\n", v)
	}
	fmt.Println()
}