# brownie test

brownie test for DeFi and Flashloan protocols
 
## software version

Ensure your `brownie` and `ganache-cli` versions are higher than mine:
```sh
ganache-cli@6.8.2
Brownie v1.12.4 - Python development framework for Ethereum
```
  
## setup steps
  
1. Replace an Infura endpoint in `brownie-config.yaml` with yours.
2. Compile contracts with the command `brownie compile`.
3. Write a test code under tests directory and run a test.
```sh
brownie test tests/test_sample.py
brownie test tests/test_defi.py
brownie test tests/test_flashloan.py
```
  
## License

This library is licensed under the MIT License.
