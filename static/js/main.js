
async function analyzeSentiment(feedback) {
    try {
        console.log('Starting sentiment analysis...');
        console.log('Feedback:', feedback);

        const response = await fetch('/analyze-sentiment', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: feedback })
        });

        console.log('API response status:', response.status);

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const responseData = await response.json();
        console.log('Response data:', responseData);

        if (responseData.success && responseData.result) {
            const result = responseData.result;
            console.log('Sentiment analysis result:', result);
            
            let englishSentiment = 'neutral';
            if (result.sentiment === 'مثبت') englishSentiment = 'positive';
            else if (result.sentiment === 'منفی') englishSentiment = 'negative';
            
            return {
                sentiment: englishSentiment,
                score: result.score,
                rawSentiment: result.sentiment  // Keep the Persian sentiment for display
            };
        } else {
            throw new Error('Invalid API response structure');
        }
    } catch (error) {
        console.error('Error during sentiment analysis:', error);
        throw error;
    }
}