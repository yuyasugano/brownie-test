pragma solidity ^0.5.0;

contract SimpleContract {
    uint256 value;

    function setValue(uint256 _value) external {
        value = _value;
    }

    function getValue() external view returns(uint256) {
        return value;
    }
}

