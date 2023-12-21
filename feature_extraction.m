function feature_extraction(audio_path, mat_path)
    % Read the audio file
    [x, fs] = audioread(audio_path);

    % Resample the audio to 16kHz
    outputFs = 16000;
    y = resample(x, outputFs, fs);

    % Choose a specific channel if there's more than one channel
    channel_to_use = 1;
    y = y(:, channel_to_use);

    % Set parameters for GTCC & MFCC computation
    overlap = round(fs * 0.02);        % Frame overlapping set to 20 ms
    windowSize = round(fs * 0.03);     % Size of hamming window set to 30 ms

    % Compute GTCC features with specified parameters
    [coeffsGT, deltaGT, deltaDeltaGT, loc] = gtcc(y, outputFs, 'OverlapLength', overlap, 'Window', hamming(windowSize), 'LogEnergy','append');
    [coeffsMF, deltaMF, deltaDeltaMF, loc] = mfcc(y, outputFs, 'OverlapLength', overlap, 'Window', hamming(windowSize), 'LogEnergy','ignore');

    % Concatenate the features into a row vector
    hybridFeatures = [mean(coeffsGT), mean(deltaGT), mean(deltaDeltaGT), mean(coeffsMF), mean(deltaMF), mean(deltaDeltaMF)];
    
    % Save the features to a MAT file
    save(fullfile(pwd, mat_path), 'hybridFeatures');
end
    