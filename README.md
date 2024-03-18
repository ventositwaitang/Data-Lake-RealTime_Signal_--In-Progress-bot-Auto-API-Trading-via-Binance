
# SMAsignal

"SMAsignal" is a Python Streaming Detection application for Long signals from exchange api

## Installation

Use the package manager [git](https://git-scm.com/) to install "SMAsignal".

```bash
git clone https://github.com/ventositwaitang/Data-Lake-RealTime_detection_signal.git
```

## Usage

1. Run [Streaming Engine](https://github.com/ventositwaitang/Data-Lake-RealTime_detection_signal/blob/main/Data_Lake_Streaming_of_Stocks_SQL_for_Signal_Streamlit.ipynb) in background for a few seconds, to accumulate market Data Lake

2. Run [Streamlit_Dashboard.ipynb](https://github.com/ventositwaitang/Data-Lake-RealTime_detection_signal/blob/main/Streamlit_Dashboard.ipynb) without Chunks starting with 'st.'

3. Make sure 'checkSMA.py' is in the same folder, run command below in [Streamlit_Dashboard.ipynb](https://github.com/ventositwaitang/Data-Lake-RealTime_detection_signal/blob/main/Streamlit_Dashboard.ipynb), The Web-dashboard App will pop-up then"
   
```bash
!streamlit run checkSMA.py
```
Click 'Get live SMA cross' to refresh signals

▲[price-range] classifier can be expand

## Example
![image](https://github.com/ventositwaitang/Data-Lake-RealTime_detection_signal/assets/75329979/b3235b31-0843-4402-b702-9855a98c2753)

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://github.com/ventositwaitang/Data-Lake-RealTime_detection_signal/blob/main/LICENSE.md)


