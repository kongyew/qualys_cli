default: build

GOOS=$(shell go env GOOS)
GOARCH=$(shell go env GOARCH)

build: always
	GO111MODULE=on 
	go build -o build/$(GOOS)/$(GOARCH)/qualys_cli

build-all: build/linux/amd64/qualys_cli build/darwin/amd64/qualys_cli

build/%/amd64/qualys_cli: always
	GOOS=$* GOARCH=amd64 go build -v -o $@ .

.PHONY: clean
clean:
	GO111MODULE=off go clean -i
	rm -rf build out docs dist


.PHONY: test
test:
	go test -v ./...

.PHONY: cover
cover:
	go test -race -coverprofile=coverage.txt ./...

.PHONY: lint
lint:
	bash .scripts/lint.sh

.PHONY: doc
doc:
	godoc -http=:6060




.PHONY: always
always: