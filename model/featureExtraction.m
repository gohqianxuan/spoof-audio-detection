% Set the folder path where audio files are located
folder = fullfile('D:\User\Downloads\DSProject_Data\PartialSpoof\database\train');

% Create an AudioDatastore object for the specified folder
ADS = audioDatastore(folder, "IncludeSubfolders", true, 'LabelSource','foldernames');

% Set the filename, sheet name, starting column for Excel output
filenameGTCC = 'GTCC_train';
filenameMFCC = 'MFCC_train';
filenameHybrid = 'GTCC-MFCC_train';

% Initialize the count as 0
count = 0;

% Set the sampling rate for the audio samples
fs = 16000;

% Initialize an array to store the features
allGT = [];
allMF = [];
allHybrid = [];

% Set parameters for GTCC & MFCC computation
overlap = round(fs * 0.02);        % Frame overlapping set to 20 ms
windowSize = round(fs * 0.03);     % Size of hamming window set to 30 ms

% Loop through the audio files in the datastore
while hasdata(ADS)

    % Count to write matrix
    count = count + 1;
    
    % Read the next audio file from the datastore
    [x, info] = read(ADS);

    % Extract the label from the foldername
    labelValue = double(string(info.Label));

    % Display the progress of file processing
    fprintf('Fraction of files read: %.2f\n', progress(ADS))
    
    if labelValue == 0
        fprintf('Processing file: spoof\n');
    else
        fprintf('Processing file: bona fide\n');
    end

    % Compute GTCC and MFCC features with specified parameters
    [coeffsGT, deltaGT, deltaDeltaGT, loc] = gtcc(x, fs,'NumCoeffs', 20, 'OverlapLength', overlap, 'Window', hamming(windowSize), 'LogEnergy','ignore');
    [coeffsMF, deltaMF, deltaDeltaMF, loc] = mfcc(x, fs,'NumCoeffs', 20, 'OverlapLength', overlap, 'Window', hamming(windowSize), 'LogEnergy','ignore');
    
    gtFeatures = [mean(coeffsGT), mean(deltaGT), mean(deltaDeltaGT), labelValue];
    mfFeatures = [mean(coeffsMF), mean(deltaMF), mean(deltaDeltaMF), labelValue];
    hybridFeatures = [mean(coeffsGT), mean(deltaGT), mean(deltaDeltaGT), mean(coeffsMF), mean(deltaMF), mean(deltaDeltaMF), labelValue];
    
    allGT = [allGT; gtFeatures];
    allMF = [allMF; mfFeatures];        
    allHybrid = [allHybrid; hybridFeatures];
    
    % Write the features to csv file when every 8000 audios are read
    if count == 8000
        writematrix(allGT, [filenameGTCC, '.csv'], 'WriteMode','append');
        writematrix(allMF, [filenameMFCC, '.csv'], 'WriteMode','append');
        writematrix(allHybrid, [filenameHybrid, '.csv'], 'WriteMode','append');
        
        count = 0;
        allGT = [];
        allMF = [];
        allHybrid = [];
    end
end
